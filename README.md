% !TEX program = pdflatex
\documentclass\[12pt]{article}
\usepackage\[margin=1in]{geometry}
\usepackage{hyperref}
\title{\LARGE\textbf{AgriSage: Your Smart Crop Advisor}}
\author{AgriSage Team}
\date{}

\begin{document}
\maketitle

\vspace{1em}
\noindent\textbf{Live Demo:} \url{[https://recommendation-system-u1iy.onrender.com/}](https://recommendation-system-u1iy.onrender.com/})

\section\*{Overview}
\noindent
AgriSage is an intelligent Flask‑based crop recommendation system that empowers farmers and agricultural planners with data‑driven insights. By analyzing key soil and climate parameters—\textbf{Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH,} and \textbf{Rainfall}—it instantly predicts the most suitable crop to cultivate under specific field conditions.

\section\*{Features}
\begin{itemize}
\item \textbf{Interactive Web UI:} Built with Flask and Jinja2 for seamless user interaction.
\item \textbf{Real‑time Predictions:} Powered by a pre‑trained Random Forest Classifier.
\item \textbf{Hyperparameter‑Tuned:} Optimized via GridSearchCV and 5‑fold cross‑validation.
\item \textbf{Robust Preprocessing:} Standard scaling and label encoding ensure model reliability.
\item \textbf{Production‑Ready:} Deployable with Gunicorn or any WSGI server.
\end{itemize}

\section\*{Repository Structure}
\noindent
\texttt{├── api/}\newline
\texttt{│   └── crop\_recommender\_app.py} \quad Flask application entry point
ewline
\texttt{├── templates/}\newline
\texttt{│   └── index.html} \quad HTML form for user inputs
ewline
\texttt{├── crop\_data.csv} \quad Original dataset
ewline
\texttt{├── Crop-Recommender.pkl} \quad Trained Random Forest model
ewline
\texttt{├── Feature-Scaler.pkl} \quad Trained StandardScaler
ewline
\texttt{├── Label-Encoder.pkl} \quad Trained LabelEncoder
ewline
\texttt{├── requirements.txt} \quad Python dependencies
ewline
\texttt{├── runtime.txt} \quad Python version for Render (python-3.8.10)
ewline
\texttt{├── render.yaml} \quad Render build configuration
ewline
\texttt{└── README.tex} \quad This file

\section\*{Installation & Setup}
\begin{enumerate}
\item Clone the repository:\newline
\texttt{git clone [https://github.com/YOUR-USERNAME/recommendation\\\_system.git}](https://github.com/YOUR-USERNAME/recommendation\_system.git})
\item Navigate into directory:\newline
\texttt{cd recommendation\_system}
\item Create a virtual environment:\newline
\texttt{python3 -m venv venv}
\item Activate the environment:\newline
\texttt{source venv/bin/activate} (macOS/Linux) or \texttt{venv\Scripts\activate} (Windows)
\item Install dependencies:\newline
\texttt{pip install -r requirements.txt}
\end{enumerate}

\section\*{Running Locally}
\noindent
Development mode (Flask built‑in server):
\begin{verbatim}
python api/crop\_recommender\_app.py
\end{verbatim}
Production mode (Gunicorn WSGI server):
\begin{verbatim}
gunicorn api.crop\_recommender\_app\:app
\end{verbatim}
Then open \url{[http://localhost:5000}](http://localhost:5000}) in your browser.

\section\*{Model Details}
\begin{itemize}
\item \textbf{Algorithm:} Random Forest Classifier
\item \textbf{Tuning:} GridSearchCV over key hyperparameters with 5‑fold CV
\item \textbf{Preprocessing:} LabelEncoder for targets, StandardScaler for features
\item \textbf{Artifacts:} Crop-Recommender.pkl, Feature-Scaler.pkl, Label-Encoder.pkl
\end{itemize}

\section\*{Deployment}
\noindent
Live on Render: \url{[https://recommendation-system-u1iy.onrender.com/}](https://recommendation-system-u1iy.onrender.com/})

\section\*{License}
\noindent
This project is licensed under the \textbf{MIT License}. See the LICENSE file for details.

\vfill
\begin{center}
Made with \textheart{ }by the AgriSage Team
\end{center}

\end{document}
