# User Wallet API

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-24-blue?style=for-the-badge&logo=docker)
![AWS](https://img.shields.io/badge/AWS-EC2-orange?style=for-the-badge&logo=amazon-aws)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-blueviolet?style=for-the-badge&logo=github-actions)

A comprehensive RESTful API for a simple user wallet system, built with a modern Python stack. This project allows for user management, wallet balance updates, and transaction history retrieval. It is fully containerized with Docker and deployed on an AWS EC2 instance with an automated CI/CD pipeline.

---

## 🚀 Live Demo

The API is live and its interactive documentation (Swagger UI) can be accessed here:

**[http://54.243.129.70/docs](http://54.243.129.70/docs)**

> ### A Note on the Demo
> This project is hosted on an AWS EC2 Free Tier instance to manage costs. The instance may be stopped periodically. If the demo link is unavailable, please feel free to email me at **aksbal2005@gmail.com**, and I will be happy to spin the server up for you.

---

## ✨ Key Features

*   **List Users:** Fetch details (name, email, phone) for all users along with their current wallet balance.
*   **Update Wallet:** Add or deduct an amount from a specific user's wallet, creating a transaction record for each operation.
*   **Fetch Transactions:** Retrieve a complete, chronologically sorted list of all wallet transactions for a specific user.

---

## 🛠️ Tech Stack

*   **Backend:** FastAPI, Uvicorn
*   **Database:** PostgreSQL
*   **ORM:** SQLAlchemy
*   **Data Validation:** Pydantic
*   **Containerization:** Docker
*   **Web Server / Reverse Proxy:** Nginx
*   **Deployment:** AWS EC2
*   **CI/CD:** GitHub Actions

---

## ⚙️ API Endpoints

The interactive Swagger UI at the [/docs](http://54.243.129.70/docs) endpoint is the best way to explore the API.

| Method | Endpoint                          | Description                               |
|--------|-----------------------------------|-------------------------------------------|
| `GET`  | `/users/`                         | Fetches all users and their wallet balance. |
| `POST` | `/users/`                         | Creates a new user and their wallet.      |
| `POST` | `/wallets/update/`                | Adds or deducts funds from a user's wallet. |
| `GET`  | `/users/{user_id}/transactions/`  | Gets all transactions for a specific user.  |

---

## 🔄 Deployment & CI/CD

This project is configured with a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline using **GitHub Actions**.

1.  **Trigger:** A `git push` to the `main` branch.
2.  **Action:** The GitHub Actions workflow automatically connects to the AWS EC2 instance via SSH.
3.  **Deployment:** The script on the server then performs the following:
    *   Pulls the latest code from the `main` branch.
    *   Installs any new dependencies from `requirements.txt`.
    *   Restarts the `Gunicorn` application service to apply the changes.

This ensures that the live application is always up-to-date with the latest version of the code.

---

## 🔧 Running Locally

To set up and run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/user-wallet.git
    cd user-wallet
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    *   Create a file named `.env` in the project root.
    *   Copy the contents of `.env.example` and fill in your local database credentials.

5.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

---

## 📧 Contact

Akshat Balyan – aksbal2005@gmail.com
