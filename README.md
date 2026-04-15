# 🍽️ AI Calorie Tracker

## 🚀 Overview

AI Calorie Tracker is a **vision-powered AI application** that analyzes food images, identifies visible items, and estimates their nutritional content using multimodal LLMs.

The system leverages a structured pipeline combining:

* Image preprocessing
* Vision-based food recognition
* Structured JSON nutrition estimation
* A user-facing Gradio interface

This project demonstrates how to build a **modular, production-oriented AI system** rather than a simple notebook prototype.

---

## 🎯 Problem Statement

Estimating calorie intake from meals is often:

* Manual
* Time-consuming
* Inaccurate

This project explores how **multimodal AI models** can automate this process by:

1. Understanding food content from images
2. Estimating portion sizes
3. Generating structured nutritional breakdowns

---

## 🧠 Solution Architecture

The system is designed as a **layered AI pipeline**, separating concerns for scalability and maintainability.

### 🔄 Flow

```
User Image
   ↓
Image Encoder Service
   ↓
Vision Service (LLM)
   ↓
Food Identification
   ↓
Nutrition Estimation (Structured JSON)
   ↓
Model Parsing + Validation
   ↓
Gradio UI Output
```

---

## 🏗️ Project Structure

```
ai_calorie_tracker/
├── app.py                      # Gradio UI
├── main.py                     # Entry point
├── config/                     # Environment & model config
├── clients/                    # OpenAI client factory
├── examples/                   # Food Example images
├── services/                   # Core AI logic
│   ├── image_encoder_service.py
│   ├── vision_service.py
│   └── nutrition_estimation_service.py
├── prompts/                    # Centralized prompt definitions
├── models/                     # Typed response models
├── utils/                      # Validation utilities
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Python**
* **OpenAI Vision Models (GPT-4o / GPT-4o-mini / GPT-5.4-mini)**
* **Gradio** (UI Layer)
* **Pillow** (Image Processing)
* **Pandas** (Data handling)
* **dotenv** (Configuration)

---

## 🧪 Features

* 📸 Upload food images via UI
* 🧠 AI-powered food recognition
* 🍽️ Nutritional breakdown (calories, protein, carbs, fat, etc.)
* 📊 Structured tabular output
* ⚠️ Error handling for malformed LLM responses
* 🧩 Modular service-based architecture

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vinishvivek/AI-Calorie-Tracker.git
cd AI-Calorie-Tracker
```

### 2. Create virtual environment

```bash
conda create -n calorie_tracker python=3.11
conda activate calorie_tracker
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
VISION_MODEL=gpt-4o
MAX_TOKENS=800
```

### 5. Run the app

```bash
python main.py
```

Then open:

```
http://127.0.0.1:7860
```

---

## ⚠️ Limitations

* Nutritional estimates are **approximate**, not medically accurate
* Model output may occasionally be:

  * incomplete (token limits)
  * slightly inconsistent
* Performance depends on:

  * image quality
  * portion visibility

---

## 🔧 Engineering Highlights

This project intentionally focuses on **AI system design**, not just model usage:

* ✅ Separation of concerns (services, clients, config)
* ✅ Prompt engineering isolation
* ✅ Structured output modeling (dataclasses)
* ✅ LLM response cleaning & parsing
* ✅ Error handling for unreliable outputs
* ✅ UI decoupled from business logic

---

## 🚀 Future Improvements

* JSON schema validation (Pydantic)
* Retry + fallback mechanisms for LLM calls
* Confidence scoring for predictions
* Meal history tracking (DB integration)
* Multi-image meal aggregation
* Cost/token monitoring layer
* Deployment (Docker + cloud hosting)

---

## 📌 Key Takeaway

This project is not just about calorie estimation.

It demonstrates how to:

> Build a **robust, modular AI application** that handles real-world issues like
> unreliable model outputs, structured parsing, and scalable architecture.

---

## 👤 Author

**Vinish Vivek**

AI Engineer | LLM Systems | Applied AI Development

---

## ⭐ If you found this useful

Consider starring the repo — or better, fork it and build your own version 🚀
