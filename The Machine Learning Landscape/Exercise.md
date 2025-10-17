## 🧩 Exercises – Chapter 1: The Machine Learning Landscape

**1. How would you define Machine Learning?**
Machine Learning is basically a way to make computers learn from data without being directly programmed. The more data it gets, the better it performs at specific tasks by finding patterns or relationships in that data.

---

**2. Can you name four types of problems where it shines?**

* Spam email detection
* Image and speech recognition
* Recommendation systems (like Netflix or YouTube)
* Predicting trends (like house prices or sales)

---

**3. What is a labeled training set?**
It’s a dataset that already has the correct answers (labels) for each input.
For example, in a spam filter, every email is marked as “spam” or “not spam.”
The model uses these examples to learn how to classify new emails.

---

**4. What are the two most common supervised tasks?**

* **Classification:** Predicting a category (like spam or not spam).
* **Regression:** Predicting a continuous value (like the price of a house).

---

**5. Can you name four common unsupervised tasks?**

* **Clustering** (grouping similar items, like customer segmentation)
* **Dimensionality Reduction** (simplifying data while keeping key info)
* **Anomaly Detection** (finding unusual patterns)
* **Association Rule Learning** (like “people who buy X also buy Y”)

---

**6. What type of Machine Learning algorithm would you use to allow a robot to walk in various unknown terrains?**

That would be **Reinforcement Learning** — the robot learns by trying, making mistakes, and getting rewards for good actions until it figures out how to walk properly.

---

**7. What type of algorithm would you use to segment your customers into multiple groups?**

That’s an **Unsupervised Learning** problem, specifically a **Clustering algorithm** like K-Means.

---

**8. Would you frame the problem of spam detection as a supervised or unsupervised learning problem?**

It’s a **Supervised Learning** problem because we already have labeled examples — emails marked as spam or not spam — that the model can learn from.

---

**9. What is an online learning system?**

An online learning system updates itself continuously as new data comes in.
It doesn’t need to be retrained from scratch every time — perfect for real-time applications.

---

**10. What is out-of-core learning?**

It’s used when the dataset is too big to fit into memory all at once.
The model loads small chunks of data, learns from them, and keeps repeating this process until it has learned from the whole dataset.

---

**11. What type of learning algorithm relies on a similarity measure to make predictions?**

That’s an **Instance-Based Learning** algorithm.
It memorizes examples and compares new data with them using a **similarity measure** like distance.
Example: **K-Nearest Neighbors (KNN)** predicts based on the most similar past instances.

---

**12. What is the difference between a model parameter and a learning algorithm’s hyperparameter?**

* **Model parameters** are what the algorithm learns automatically during training (like weights in Linear Regression).
* **Hyperparameters** are the settings we choose before training (like learning rate, number of neighbors, or regularization strength).
  Basically, parameters are learned; hyperparameters are chosen.

---

**13. What do model-based learning algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?**

* They search for **the best model parameters** that minimize the error between predictions and actual results.
* The most common strategy is to **define a cost function** (like mean squared error) and use an **optimization algorithm** (like gradient descent) to find the lowest point.
* Once trained, they use the learned parameters to **make predictions** on new data.

---

**14. Can you name four of the main challenges in Machine Learning?**

1. Not enough training data
2. Nonrepresentative or biased data
3. Poor-quality data (noise, missing values)
4. Overfitting and underfitting

---

**15. If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?**

That’s **overfitting** — the model learned the training data too well, including noise.
**Solutions:**

1. Simplify the model (use fewer features or smaller architecture)
2. Get more training data
3. Use regularization (like L1 or L2)

---

**16. What is a test set, and why would you want to use it?**

A **test set** is a separate portion of the data that you keep aside to check how well your final model performs on unseen data.
It helps you know if your model can **generalize** in the real world.

---

**17. What is the purpose of a validation set?**

The **validation set** is used during model development to test different models or hyperparameter settings before finalizing one.
It helps you tune and compare models **without touching the test set**.

---

**18. What is the train-dev set, when do you need it, and how do you use it?**

You create a **train-dev set** when your validation and test sets come from slightly different distributions.
It’s a small part of your training data that helps you spot data mismatch issues.
You use it to check whether the model’s poor performance is due to overfitting or data differences.

---

**19. What can go wrong if you tune hyperparameters using the test set?**

You’ll accidentally make your model **fit the test data**, which ruins its purpose.
It’ll look like your model performs well, but it won’t generalize to new data.
Basically, you’re “leaking” test data information into training, which leads to **overfitting on the test set**.
