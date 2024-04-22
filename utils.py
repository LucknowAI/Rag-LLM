import json
import os


def write_to_json(data, filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            existing_data = json.load(file)
        # Check if the email already exists in the file
        if "user" in data:
            existing_emails = [
                entry["user"] for entry in existing_data if "user" in entry
            ]
            if data["user"] in existing_emails:
                return
        existing_data.append(data)
        with open(filename, "w") as file:
            json.dump(existing_data, file, indent=4)
    else:
        with open(filename, "w") as file:
            json.dump([data], file, indent=4)


def fc(user_id):
    email_filename = "queries" + f"\{user_id}.json"
    return email_filename


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)