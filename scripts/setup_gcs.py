"""
Setup script — uploads mock data to GCS and optionally configures Vertex AI Search.

Usage:
    python scripts/setup_gcs.py

Requirements:
    - GCP_PROJECT_ID set in .env
    - GCS_BUCKET_NAME set in .env
    - Application Default Credentials: `gcloud auth application-default login`
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

try:
    from google.cloud import storage
except ImportError:
    print("google-cloud-storage not installed. Run: pip install google-cloud-storage")
    sys.exit(1)

PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "cortexiom-orchestrator")
REGION = os.environ.get("GCP_REGION", "us-central1")
BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME", "cortexiom-orchestrator-data")
DATA_DIR = Path(__file__).parent.parent / "data"


def create_bucket_if_not_exists(client: storage.Client, bucket_name: str) -> storage.Bucket:
    bucket = client.bucket(bucket_name)
    if not bucket.exists():
        bucket = client.create_bucket(bucket_name, location=REGION)
        print(f"Created bucket: gs://{bucket_name}")
    else:
        print(f"Bucket already exists: gs://{bucket_name}")
    return bucket


def upload_data_files(bucket: storage.Bucket) -> list[str]:
    uploaded = []
    for file_path in sorted(DATA_DIR.rglob("*.md")):
        # GCS object path mirrors local path relative to data/
        relative = file_path.relative_to(DATA_DIR)
        blob_name = f"compliance-data/{relative.as_posix()}"
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(str(file_path), content_type="text/markdown")
        print(f"  Uploaded: {blob_name}")
        uploaded.append(f"gs://{bucket.name}/{blob_name}")
    return uploaded


def configure_vertex_ai_search(gcs_uris: list[str]) -> None:
    ds_id = os.environ.get("VERTEX_AI_SEARCH_DATA_STORE_ID", "")
    if not ds_id:
        print(
            "\nVERTEX_AI_SEARCH_DATA_STORE_ID not set — skipping Vertex AI Search setup.\n"
            "To enable semantic search:\n"
            "  1. Go to: https://console.cloud.google.com/vertex-ai/search\n"
            "  2. Create a new Search data store (type: Unstructured)\n"
            "  3. Import from GCS: gs://{BUCKET_NAME}/compliance-data/\n"
            "  4. Add VERTEX_AI_SEARCH_DATA_STORE_ID=<id> to .env"
        )
        return

    print(f"\nVertex AI Search data store ID: {ds_id}")
    print("To import data into the data store:")
    print(f"  gcloud alpha discovery-engine datastores import documents \\")
    print(f"    --datastore={ds_id} \\")
    print(f"    --location=global \\")
    print(f"    --gcs-source=gs://{BUCKET_NAME}/compliance-data/ \\")
    print(f"    --project={PROJECT_ID}")


def main() -> None:
    print(f"Setting up GCS for project: {PROJECT_ID}")
    print(f"Bucket: {BUCKET_NAME}\n")

    client = storage.Client(project=PROJECT_ID)
    bucket = create_bucket_if_not_exists(client, BUCKET_NAME)

    print("\nUploading data files…")
    uris = upload_data_files(bucket)
    print(f"\nUploaded {len(uris)} files to gs://{BUCKET_NAME}/compliance-data/")

    configure_vertex_ai_search(uris)

    print("\nSetup complete.")
    print(f"\nNext steps:")
    print(f"  1. Add CORTEXIOM_API_KEY to .env (get key at developers.cortexiom.com)")
    print(f"  2. Run: streamlit run frontend/app.py")


if __name__ == "__main__":
    main()