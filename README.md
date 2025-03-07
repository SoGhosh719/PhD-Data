# PhD-Data

Here’s your complete **README.md** file combining all the details in Markdown format:

```markdown
# 🔍 University Homepage Finder

This project **automates the process of finding university homepages** using multiple search methods, including:
- **SerpAPI**
- **Bing Search API**
- **Google Custom Search API**
- **DuckDuckGo API**
- **Google Scraping (No API)**
- **Static University Database (CSV)**

---

## 🔹 Goal of the Project
- Extract a list of **universities in the US** from a CSV file.
- Automate **homepage retrieval** using multiple search engines.
- Compare different methods for **accuracy, reliability, and scalability**.

---

## 📂 **Project Structure**
```plaintext
/workspaces/PhD-Data/
│── universities_list.csv                  # Input: List of university names
│── universities_with_homepages.csv        # Output: Final results with homepages
│── find_homepage_serpapi.py               # SerpAPI method
│── find_homepage_bing.py                  # Bing API method
│── find_homepage_google_cse.py            # Google Custom Search API method
│── find_homepage_duckduckgo.py            # DuckDuckGo API method
│── find_homepage_google_scraping.py       # Google Scraping (No API)
│── find_homepage_database.py              # Static CSV lookup method
│── README.md                              # Documentation
```

---

## ⚙️ **Setup & Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/PhD-Data.git
cd PhD-Data
```

### **2️⃣ Install Dependencies**
```sh
pip install requests beautifulsoup4 pandas google-search-results
```

### **3️⃣ Get API Keys**
Some methods require **API keys**:

| **Method**            | **API Required?** | **Get API Key From** |
|----------------------|----------------|----------------|
| **SerpAPI**         | ✅ Yes         | [SerpAPI](https://serpapi.com/) |
| **Bing API**        | ✅ Yes         | [Azure Portal](https://portal.azure.com/) |
| **Google CSE API**  | ✅ Yes         | [Google API Console](https://developers.google.com/custom-search/v1/overview) |
| **DuckDuckGo API**  | ❌ No          | No API needed |
| **Google Scraping** | ❌ No          | No API needed (but risky) |
| **Static Database** | ❌ No          | Uses local CSV file |

🔹 **Store API Keys as Environment Variables** (Optional)
```sh
export SERP_API_KEY="your_serpapi_key"
export BING_API_KEY="your_bing_api_key"
export GOOGLE_API_KEY="your_google_api_key"
export CSE_ID="your_google_cse_id"
```

---

## 🚀 **Usage**
Each method is stored in a **separate Python file**. Run any script to fetch university homepages.

### **1️⃣ Run SerpAPI Method**
```sh
python find_homepage_serpapi.py
```

### **2️⃣ Run Bing API Method**
```sh
python find_homepage_bing.py
```

### **3️⃣ Run Google CSE API Method**
```sh
python find_homepage_google_cse.py
```

### **4️⃣ Run DuckDuckGo API Method**
```sh
python find_homepage_duckduckgo.py
```

### **5️⃣ Run Google Scraping (No API)**
```sh
python find_homepage_google_scraping.py
```

### **6️⃣ Use Static University Database**
```sh
python find_homepage_database.py
```

---

## 🔹 Work Breakdown

### **1️⃣ Data Preparation**
- Created **`universities_list.csv`**, containing **216 universities**.
- Manually verified and structured the data into:
  - **Name** (University Name)
  - **City**
  - **State**
  - **Control** (Public/Private)

### **2️⃣ Implementing Multiple Search Methods**
You have implemented **5 different ways** to extract university homepages:

| **Method**           | **Software/Tool Used**  | **API Key Required?** | **Free Searches** | **Implementation File** |
|----------------------|----------------|----------------|--------------|--------------------------|
| **SerpAPI**         | Python + SerpAPI SDK | ✅ Yes | 100/month | `find_homepage_serpapi.py` |
| **Bing Search API** | Python + Requests | ✅ Yes | 5,000/month | `find_homepage_bing.py` |
| **Google CSE API**  | Python + Requests | ✅ Yes | 100/day | `find_homepage_google_cse.py` |
| **DuckDuckGo API**  | Python + Requests | ❌ No | Unlimited | `find_homepage_duckduckgo.py` |
| **Google Scraping** | Python + BeautifulSoup | ❌ No (Risky) | Unlimited | `find_homepage_google_scraping.py` |
| **Static Database** | Python + Pandas | ❌ No | Unlimited | `find_homepage_database.py` |

### **3️⃣ Automating Data Extraction**
- Each Python script reads university names from **`universities_list.csv`**.
- Searches for the **official homepage** using the respective method.
- Saves results into **separate CSV files**:
  - `universities_with_serpapi.csv`
  - `universities_with_bing.csv`
  - `universities_with_google_cse.csv`
  - `universities_with_duckduckgo.csv`
  - `universities_with_google_scraping.csv`
  - `universities_with_database.csv`

### **4️⃣ Handling Errors & Rate Limits**
- **Added error handling** for missing data, API failures, and rate limits.
- **Implemented API request delays** to prevent getting blocked.

---

## 📊 **Comparison of Methods**
| **Method**           | **Free Searches** | **Accuracy**  | **API Required?** |
|----------------------|----------------|--------------|----------------|
| **SerpAPI**         | 100/month      | ✅✅✅✅✅ | ✅ Yes |
| **Bing API**        | 5,000/month    | ✅✅✅✅  | ✅ Yes |
| **Google CSE API**  | 100/day        | ✅✅✅✅✅ | ✅ Yes |
| **DuckDuckGo API**  | Unlimited      | ✅✅✅  | ❌ No  |
| **Google Scraping** | Unlimited (Risky) | ✅✅✅✅✅ | ❌ No  |
| **Static Database** | Unlimited      | ✅✅✅✅ | ❌ No  |

---

## 🔹 Challenges & Solutions
| **Challenge** | **Solution** |
|--------------|-------------|
| **Limited free API requests** | Used multiple services to distribute queries |
| **Google blocking web scraping** | Used DuckDuckGo API as a backup |
| **CSV formatting issues** | Fixed BOM encoding and column name mismatches |
| **SerpAPI and Bing required API keys** | Automated key management using environment variables |
| **Slow execution for large lists** | Optimized queries & added multiprocessing (future improvement) |

---

## 🔹 Final Outcome
- ✅ **Automated** homepage retrieval for **216 universities**.
- ✅ Successfully used **5 different search methods**.
- ✅ **Compared accuracy** of different APIs & search engines.
- ✅ **Created modular Python scripts** for easy reusability.
- ✅ **Stored extracted data in structured CSV files**.

---

## 🔥 **Contributing**
Feel free to contribute by adding **more search methods** or **improving the existing scripts**.

### **To Contribute**
1. **Fork the repo**
2. **Create a feature branch** (`git checkout -b feature-new-method`)
3. **Commit your changes** (`git commit -m "Added new search method"`)
4. **Push to your branch** (`git push origin feature-new-method`)
5. **Create a Pull Request**

---

## 📜 **License**
This project is open-source and licensed under the **MIT License**.

---

## 🎯 **Author**
👨‍💻 **Soumyabrata Ghosh**  
📧 **soumyabrata11411@gmail.com**  
🔗 **[Your GitHub](https://github.com/SoGhosh719)**  

---

🚀 **Happy Searching!**
