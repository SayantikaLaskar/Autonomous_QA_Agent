# QA Agent Video Demonstration Script
**Duration: 5-10 minutes**

## 🎬 **Pre-Recording Setup**

### What You Need:
- Screen recording software (OBS Studio, Camtasia, or built-in screen recorder)
- Clean desktop/browser
- Project running on localhost:8501
- Sample files ready for upload

### Before You Start Recording:
1. **Close unnecessary applications**
2. **Clear browser cache/history** 
3. **Test run the application** to ensure everything works
4. **Prepare your voice** - speak clearly and at moderate pace
5. **Have water nearby** for dry mouth

---

## 🎯 **Video Script Outline**

### **INTRO (30 seconds)**
**[Show desktop with project folder]**

**Say:** 
> "Hi! Today I'm demonstrating an Autonomous QA Agent that generates test cases and Selenium scripts from project documentation. This system reads your docs, builds a knowledge base, and creates automated tests grounded in your actual requirements - no hallucinations!"

**Action:** 
- Show project folder structure briefly
- Open terminal

---

### **SECTION 1: Starting the Application (45 seconds)**

**[Terminal visible]**

**Say:** 
> "Let's start by launching our QA Agent. I'll run the start script which launches both the FastAPI backend and Streamlit frontend."

**Action & Commands:**
```bash
# Navigate to project directory
cd qa-agent

# Install dependencies (if needed)
pip install -r requirements.txt

# Start the application
python start_app.py
```

**Say while waiting:**
> "The application is starting up. It launches FastAPI on port 8000 for the backend services and Streamlit on port 8501 for our user interface."

**Action:**
- Wait for both servers to start
- Open browser to http://localhost:8501

---

### **SECTION 2: Application Overview (30 seconds)**

**[Streamlit interface visible]**

**Say:**
> "Here's our QA Agent interface. We have three main phases: First, we upload documents and HTML to build our knowledge base. Then we generate test cases from that knowledge. Finally, we convert test cases into executable Selenium scripts."

**Action:**
- Point to different sections of the UI
- Show the clean, intuitive layout

---

### **SECTION 3: Uploading Documents (90 seconds)**

**[Document Upload Section]**

**Say:**
> "Let's start by uploading our support documents. These contain the business rules, UI guidelines, and specifications that will ground our test generation."

**Action:**
1. **Upload support documents one by one:**
   - `product_specs.md` - "This contains our business rules like discount codes"
   - `ui_ux_guide.txt` - "UI guidelines and validation rules"  
   - `api_endpoints.json` - "API specifications"
   - `business_requirements.md` - "Core business requirements"
   - `test_scenarios.md` - "Existing test scenarios"

**Say for each upload:**
> "I'm uploading [filename] which contains [brief description of content]"

2. **Upload HTML file:**

**Say:**
> "Now I'll upload our target web application - a checkout.html file that represents an e-commerce checkout page with forms, validation, and payment processing."

**Action:**
- Upload `checkout.html`
- Show the file appears in the interface

**Say:**
> "Perfect! All our documents are uploaded. You can see the system has detected 5 support documents and our HTML target file."

---

### **SECTION 4: Building Knowledge Base (60 seconds)**

**[Knowledge Base Section]**

**Say:**
> "Now let's build our knowledge base. This process will parse all documents, chunk the text, generate embeddings, and store everything in a vector database for intelligent retrieval."

**Action:**
- Click "Build Knowledge Base" button
- Show loading indicator

**Say while processing:**
> "The system is now processing our documents. It's extracting text, creating semantic chunks, and building vector embeddings using a transformer model. This creates a searchable knowledge base that our AI agent can query to generate grounded test cases."

**Action:**
- Wait for "Knowledge Base Built Successfully!" message
- Show success indicator and document count

**Say:**
> "Excellent! Our knowledge base is ready with [X] document chunks. The system can now intelligently retrieve relevant information to generate test cases."

---

### **SECTION 5: Generating Test Cases (90 seconds)**

**[Test Case Generation Section]**

**Say:**
> "Now for the exciting part - generating test cases! I'll request test cases for different features of our checkout page."

**Action & Examples:**

1. **First Query:**
**Type:** "Generate test cases for the discount code feature"
**Say:** "Let me generate test cases for the discount code functionality."

**Action:**
- Click "Generate Test Cases"
- Show loading
- Display generated test cases

**Say while reviewing results:**
> "Look at this! The system generated comprehensive test cases including positive tests for valid codes, negative tests for invalid codes, and edge cases. Notice how each test case references the source document - it's grounded in our product_specs.md file."

2. **Second Query:**
**Type:** "Generate test cases for form validation"
**Say:** "Let me also generate test cases for form validation."

**Action:**
- Generate and show results
- Point out the grounding in documentation

**Say:**
> "Perfect! These test cases cover email validation, required fields, and error message display - all based on our UI/UX guidelines document."

---

### **SECTION 6: Selecting and Generating Selenium Script (90 seconds)**

**[Script Generation Section]**

**Say:**
> "Now let's convert one of these test cases into an executable Selenium script. I'll select a test case and generate the automation code."

**Action:**
1. **Select a test case** (e.g., discount code test)
2. **Click "Generate Selenium Script"**

**Say while processing:**
> "The system is now analyzing our HTML structure, understanding the test case requirements, and generating Python Selenium code with proper selectors and assertions."

**Action:**
- Show the generated script
- Scroll through the code

**Say while reviewing code:**
> "Fantastic! Look at this clean, executable Selenium script. It includes proper imports, WebDriver setup, element selectors that match our actual HTML, and assertions that verify the expected behavior. The selectors are based on the real HTML structure we uploaded."

**Action:**
- Point out key parts:
  - WebDriver setup
  - Element selectors (IDs, names, CSS)
  - Test steps
  - Assertions
  - Error handling

**Say:**
> "This script is ready to run! It would actually test our checkout page by applying the discount code and verifying the price reduction."

---

### **SECTION 7: Demonstrating Another Feature (60 seconds)**

**[Optional - if time allows]**

**Say:**
> "Let me quickly show another example - generating a script for form validation."

**Action:**
- Select form validation test case
- Generate script
- Show different selectors and validation logic

**Say:**
> "Notice how this script tests form validation by entering invalid data and checking for error messages. The selectors and validation logic are all based on our uploaded documents and HTML structure."

---

### **SECTION 8: Wrap-up and Key Benefits (45 seconds)**

**[Show full interface]**

**Say:**
> "Let's recap what we've accomplished. We uploaded project documentation, built an intelligent knowledge base, generated comprehensive test cases grounded in our actual requirements, and created executable Selenium scripts - all automatically!"

**Action:**
- Scroll through generated test cases
- Show generated scripts

**Say:**
> "The key benefits are: First, no hallucinations - everything is grounded in your actual documentation. Second, comprehensive coverage - it generates both positive and negative test cases. Third, ready-to-run code - the Selenium scripts use real selectors from your HTML. And fourth, it's fast and scalable for any web application."

**Final Say:**
> "This QA Agent transforms your documentation into a comprehensive testing suite, saving hours of manual test writing while ensuring accuracy and completeness. Thanks for watching!"

---

## 🎥 **Recording Tips**

### **Voice & Delivery:**
- Speak clearly and at moderate pace
- Use enthusiastic but professional tone
- Pause briefly between sections
- Emphasize key benefits and features

### **Screen Recording:**
- Use 1080p resolution minimum
- Keep mouse movements smooth and deliberate
- Highlight important UI elements
- Zoom in on code when needed

### **Technical Tips:**
- Test everything before recording
- Have backup plans if something fails
- Keep browser zoom at 100%
- Close notification popups

### **Editing Notes:**
- Cut out long loading times (show start, then cut to completion)
- Add text overlays for key points
- Use smooth transitions between sections
- Include intro/outro slides if desired

---

## 🚀 **Post-Recording Checklist**

- [ ] Review for audio quality
- [ ] Check for any technical errors shown
- [ ] Verify all key features were demonstrated
- [ ] Add captions if needed
- [ ] Export in appropriate format (MP4 recommended)
- [ ] Test playback on different devices

---

## 📝 **Backup Talking Points**

If you need to fill time or something goes wrong:

**About the Technology:**
- "This uses FastAPI for high-performance backend services"
- "Streamlit provides a clean, intuitive interface"
- "Vector embeddings enable semantic search of documentation"
- "The system prevents AI hallucinations by grounding in real docs"

**About the Benefits:**
- "Saves QA teams hours of manual test case writing"
- "Ensures test coverage matches actual requirements"
- "Generates maintainable, readable Selenium code"
- "Scales to any web application or documentation set"

**If Technical Issues Occur:**
- "In a real scenario, this would complete in [X] seconds"
- "The system is designed to handle much larger document sets"
- "This works with any HTML structure or documentation format"