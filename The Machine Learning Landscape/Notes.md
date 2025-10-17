# Chapter 1: The Machine Learning Landscape

## What Is Machine Learning?

* **Machine Learning (ML)** is a field of computer science where systems **learn from data** instead of being explicitly programmed.
* A program is considered to “learn” if it improves its performance on a given task **T**, based on **experience E**, measured by some **performance metric P**.

  * Example: A spam filter learns to classify emails (T) by analyzing past labeled emails (E) and improving its accuracy (P).

---

## Why Use Machine Learning?

* Traditional programming requires explicit rules.
* ML is used when:

  * Rules are **too complex to define manually** (e.g., speech recognition, image classification).
  * You need to **adapt** to new data or patterns automatically.
  * You want to **discover patterns or insights** in large datasets.
* Enables automation of decision-making and predictions.

---

## Examples of Applications

* Email spam filtering
* Speech and image recognition
* Recommender systems (Netflix, YouTube, etc.)
* Fraud detection
* Medical diagnosis
* Autonomous vehicles

Machine Learning powers most modern AI systems.

---

## Types of Machine Learning Systems

ML systems can be categorized by how they learn, how they operate, and how they generalize.

### 1. Supervised vs Unsupervised Learning

**Supervised Learning**

* Trained on **labeled data** (input → desired output).
* The model learns the mapping between inputs and outputs.
* Common algorithms:

  * Linear Regression
  * Logistic Regression
  * Decision Trees
  * Random Forests
  * Support Vector Machines (SVMs)
* Examples:

  * Predicting house prices
  * Email spam detection

**Unsupervised Learning**

* Trained on **unlabeled data** — the model finds patterns or structure by itself.
* Common algorithms:

  * Clustering (K-Means, Hierarchical)
  * Dimensionality Reduction (PCA)
  * Association Rule Learning
* Examples:

  * Customer segmentation
  * Market basket analysis

**Semi-supervised Learning**

* Mix of labeled and unlabeled data (e.g., Google Photos uses a few labeled faces to organize all photos).

**Reinforcement Learning**

* The agent learns by **trial and error**, receiving **rewards or penalties** for actions.
* Used in game-playing AI, robotics, and self-driving cars.

---

### 2. Batch and Online Learning

**Batch Learning**

* The model is trained using the **entire dataset at once**.
* Must be retrained from scratch when new data arrives.
* Suitable when data is static and training can be done offline.

**Online Learning**

* The model learns **incrementally**, updating itself as new data arrives.
* Useful for real-time systems and large data streams.
* Risk: Can be affected by “bad” or “noisy” incoming data.

---

### 3. Instance-Based vs Model-Based Learning

**Instance-Based Learning**

* Memorizes examples and compares new data to them.
* Uses **similarity measures** (e.g., distance metrics like Euclidean distance).
* Example: K-Nearest Neighbors (KNN).

**Model-Based Learning**

* Builds a model that generalizes from training data.
* Example: Linear Regression learns a mathematical relationship between features and target.

---

## Main Challenges of Machine Learning

### 1. Insufficient Quantity of Training Data

* ML models need **a lot of quality data** to learn well.
* Small datasets → poor generalization.

### 2. Nonrepresentative Training Data

* Data must **represent real-world scenarios**.
* Biased or skewed data leads to inaccurate models.

### 3. Poor-Quality Data

* Missing values, noise, and errors can harm performance.
* Data cleaning is essential.

### 4. Irrelevant Features

* Only useful features should be included.
* **Feature selection and engineering** are key steps.

### 5. Overfitting the Training Data

* The model learns **noise and details** in training data too well.
* Performs great on training data but poorly on new data.
* Solutions:

  * Simplify the model
  * Use regularization
  * Get more data

### 6. Underfitting the Training Data

* The model is **too simple** to capture underlying patterns.
* Solutions:

  * Use a more complex model
  * Reduce regularization
  * Add better features

---

## Stepping Back

* Always keep your end goal in mind: building a model that **generalizes well** to unseen data.

---

## Testing and Validating

* Data is split into:

  * **Training set** → for training
  * **Test set** → for evaluating performance
* Performance metrics (like accuracy, RMSE, precision) show how well the model performs.

---

## Hyperparameter Tuning and Model Selection

* **Hyperparameters**: Settings that control how the model learns (e.g., learning rate, number of trees).
* Use techniques like **Grid Search** or **Random Search** to find the best hyperparameters.
* Evaluate using **cross-validation**.

---

## Data Mismatch

* When the training data and real-world (production) data come from **different distributions**, performance drops.
* Always monitor and retrain the model with updated data.