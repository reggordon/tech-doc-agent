
# **AI-Powered Document Builder (Dockerized)**

## **Overview**
This app allows you to generate **PDF** and **DOCX** technical documents from **Google Docs** content. The app integrates with **Google Drive** and **Google Docs API** to fetch document content and uses **WeasyPrint** and **python-docx** to convert and save the content in PDF and DOCX formats.

The application is **Dockerized** for easy setup and consistent execution across different environments.

## **Features**
- Fetch content from a **single Google Doc**
- Convert the fetched content into **PDF** and **DOCX** files.
- Save the generated documents to the `data/output_docs/` directory.
- Docker-based setup for ease of installation and execution.

## **Installation (Docker)**git status
Follow these steps to set up the app using Docker:

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/tech-doc-agent.git
cd tech-doc-agent
```

### **2. Build the Docker Image**
First, **build the Docker image** from the `Dockerfile`:

```bash
docker build -t tech-doc-agent .
```

This will install all the dependencies inside the Docker container and set up the environment.

### **3. Set Up Google API Credentials**
1. Go to the **[Google Cloud Console](https://console.cloud.google.com/)** and enable the **Google Drive API** and **Google Docs API**.
2. Create **OAuth 2.0 Client Credentials** and download the `credentials.json` file.
3. Place the `credentials.json` file in the project root directory (on your local machine).
   - This file will be **copied into the Docker container** during the build process.

### **4. Run the Docker Container**
Once the image is built, you can **run the Docker container** with the following command:

```bash
docker run -p 8501:8501 -v $(pwd)/data:/app/data tech-doc-agent
```

- **`-p 8501:8501`**: Maps port 8501 inside the container to port 8501 on your local machine, which is used by Streamlit.
- **`-v $(pwd)/data:/app/data`**: Mounts the local `data` folder to the `/app/data` directory inside the container, so the generated documents can be saved locally.

### **5. Access the Application**
After running the Docker container, the app should be accessible at:

```
http://localhost:8501
```

The app allows you to interact with the **Streamlit UI** for generating documents from Google Docs.

## **Using the App**
1. **Authentication**: Upon first use, the app will prompt you to authenticate with Google and allow access to Google Drive and Docs.
2. **Input Google Doc ID**: Enter the **Google Doc ID** or provide a **Google Drive folder ID** to scrape multiple Google Docs.
3. **Select Document Type**: Choose the type of document you want to generate (e.g., **PRD**, **Technical Specification**, **User Guide**).
4. **Generate Documents**: Click the **Generate Document** button to fetch the content and generate the document in **PDF** and **DOCX** format.
5. **Download**: After the document is generated, you can download it from the `data/output_docs/` folder.

## **File Structure**
- **/data/output_docs/**: Folder where the generated documents (PDF and DOCX) are saved.
- **ui.py**: Streamlit UI for user interaction.
- **tools/**: Contains the helper functions for interacting with Google Docs and generating PDF/DOCX files.
- **Dockerfile**: Docker configuration for building the app container.
- **requirements.txt**: Python dependencies required for the app (used in Docker build).

## **Troubleshooting**
- **Authentication Errors**: Ensure you are using the correct **credentials.json** file, and that the Google APIs are enabled.
- **Missing Files**: Ensure that the `data/output_docs/` folder exists and is writable. Use `chmod +w data/output_docs/` to fix permissions if needed.
- **Permission Issues**: If you have problems with file access or permissions, ensure that the `data/output_docs/` folder exists in your local directory.

## **Future Enhancements**
- Cloud deployment for scalability (e.g., **AWS**, **Heroku**).
- Add support for other document formats like **HTML** or **Markdown**.
- Implement background processing for document generation.

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Key Changes:**
- The app is **Dockerized** for easy deployment.
- The **Docker setup** is the focus, reducing the need for manual setup of Python dependencies via `pip`.

---

Let me know if you'd like to adjust anything further or add additional details!
