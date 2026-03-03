import json
import os

def main():
    # Force the path to the current working directory (project root)
    target_path = os.path.join(os.getcwd(), "output.json")
    
    result = {
        "status": "success",
        "processed": True,
        "message": "Harbor Trial Completed"
    }

    try:
        with open(target_path, "w") as f:
            json.dump(result, f)
        print(f"Successfully created: {target_path}")
    except Exception as e:
        print(f"Failed to write file: {e}")

if __name__ == "__main__":
    main()