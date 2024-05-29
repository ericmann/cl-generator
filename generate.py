from openai import OpenAI
import PyPDF2
import sys
client = OpenAI()

system_prompt = (
    "You are a world-class software engineer and engineering manager."
    "Answer in a direct, concise, and professional tone directed at a recruiter or hiring manager."
    "Your audience is highly technical and looking for outstanding talent; be very specific."
)

# Parse resume
text = ""
with open('resume.pdf', 'rb') as resume:
    reader = PyPDF2.PdfReader(resume)
    for page in reader.pages:
        text += page.extract_text()

job_name = sys.argv[1]

job_text = ""
with open(f"jobs/{job_name}.txt", 'r') as job:
    job_text = job.read()

prompt = (
    f"You are a job candidate with the following resume: {text}"
    f"You are applying for a job with the following description of the role and qualifications: {job_text}"
    "Write a detailed cover letter for your application explaining why you are the best fit for the role and why."
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt}
  ]
)

with open(f"output/{job_name}.txt", 'w') as output:
    output.write(completion.choices[0].message.content)