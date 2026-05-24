# AgencyTech

## Frontend

```bash
cd frontend
npm install
npx expo start

## Backend

cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --host 0.0.0.0 --reload