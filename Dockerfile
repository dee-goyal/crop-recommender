# Use a lightweight Python 3.8 base
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy and install only Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the port Render will use
ENV PORT 10000
EXPOSE 10000

# Start the app with Gunicorn
CMD ["gunicorn", "crop_recommender_app:app", "-b", "0.0.0.0:10000"]
