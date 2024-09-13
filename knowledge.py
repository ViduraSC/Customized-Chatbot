import json

# Define a more detailed custom knowledge base
custom_knowledge = {
    "company_name": "Vertex AI Solutions",
    "industry": "Data Science & AI Solutions",
    "founder": "Vidura Chathuranga",
    "company_overview": "Vertex AI Solutions is a leading provider of data science and artificial intelligence-driven services, dedicated to helping businesses harness the full potential of their data. We specialize in AI model development, predictive analytics, and cloud-based automation solutions that enhance operational efficiency and drive business growth across industries.",
    "target_industries": "Healthcare, Finance, Retail, Manufacturing and Logistics",
    "services": [
        {
            "service_name": "Custom AI Model Development & Integration",
            "description": "We design and implement tailored AI models that suit your business needs, from predictive analytics to machine learning models and NLP-powered systems. Our solutions are scalable, customizable, and focused on solving real business challenges."
        },
        {
            "service_name": "Automation & Process Optimization",
            "description": "Using the power of AI, we automate routine processes, minimizing human errors and increasing operational efficiency. We create intelligent systems and robotic process automation (RPA) to streamline workflows."
        },
        {
            "service_name": "Cloud Integration",
            "description": "Our AI models are cloud-ready and integrate seamlessly into existing infrastructures. We support major platforms like AWS, Azure, and Google Cloud to ensure smooth AI deployment and scalability."
        },
        {
            "service_name": "Predictive Analytics & Business Intelligence",
            "description": "We help businesses leverage their data by building advanced predictive models that offer insights into customer behavior, market trends, and operational performance, driving informed decision-making."
        },
        {
            "service_name": "Data Engineering Solutions",
            "description": "We design robust data engineering pipelines that handle large-scale data processing and automation, enabling businesses to focus on insights and innovation instead of infrastructure management."
        }
    ],

    "faq": [
        {
            "question": "What industries do you specialize in?",
            "answer": "We specialize in a wide range of industries, including healthcare, finance, retail, manufacturing, and logistics, offering tailored AI solutions for each sector's unique challenges."
        },
        {
            "question": "How do you ensure data privacy and security?",
            "answer": "At Vertex AI Solutions, we prioritize data security through industry-leading practices such as encryption, compliance with data protection regulations, and secure cloud infrastructure."
        },
        {
            "question": "What kind of AI models do you develop?",
            "answer": "We develop a variety of AI models including predictive analytics, natural language processing (NLP), computer vision, and machine learning models, tailored to meet specific business requirements."
        }
    ],
    "achievements": [
        "Implemented AI-driven automation systems across 50+ global retail chains, including Walmart, leading to a 20% improvement in supply chain efficiency.",
        "Developed predictive models for McDonald's that optimized inventory management, reducing waste by 15% across multiple regions.",
        "Enabled real-time customer analytics for a Fortune 500 finance company, enhancing decision-making processes and improving customer engagement by 30%.",
        "Delivered a personalized recommendation engine for Keells supermarket chain, increasing conversion rates by 18%.",
        "Created a chatbot with advanced NLP for DHL, streamlining customer service operations and reducing response time by 40%."
    ],
    "contact_information": {
        "email": "contact@vertexaisolutions.com",
        "phone": "+94 112-565669",
        "location": "No 66, Kithyakara Rd, Colombo 010000, Sri Lanka"
    }
}


# Save the custom knowledge to a file
with open('custom_knowledge.json', 'w') as file:
    json.dump(custom_knowledge, file)
