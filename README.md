This project predicts obesity levels based on demographic and lifestyle data. The workflow covers data analysis, model training, evaluation, and deployment. The best-performing model is served in two ways:
- FastAPI: for REST API prediction endpoints.
- Streamlit: for a simple interactive UI that allows users to input data and get predictions locally.

Workflow
1. Exploratory Data Analysis (EDA)
   - Checked missing values, data distribution, and correlations.
   - Visualized lifestyle-related factors (e.g., age, diet, physical activity) against obesity levels.
2. Data Splitting
   - Divided dataset into train and test sets.
3. Modeling with Pipelines
   - Implemented pipelines for preprocessing and training.
   - Models trained: XGBoost, Support Vector Machine (SVM)
4. Model Comparison
   - Compared performance on the test set.
   - SVM achieved the highest accuracy (0.94).
5. Deployment
   - FastAPI: Served SVM model as a REST API with interactive Swagger docs.
   - Streamlit: Built a user-friendly interface for local testing, allowing users to enter feature values and view predictions directly.

Results:
- Best Model: Support Vector Machine (SVM)
- Accuracy: 94%
- Deployment: FastAPI endpoints + Streamlit UI
