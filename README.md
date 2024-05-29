# Coverletter Generator

Add your resume as `resume.pdf` to the root of this project.

Export your OpenAI API key as `OPENAI_API_KEY` (use `.env.example` as an example but ensure things are available at the command line).

Create a virtual environment and install dependencies:

```
python3 -m virtualenv .venv
source .venv/bin/activate
python -m pip install requirements.txt
```

Create text files representing the jobs to which you wish to apply in the `/jobs` directory. Each file should start with the following header:

```
Role: <<role name>>
Employer: <<employer name>>
```

Then should copy/paste the details of the job posting from LinkedIn/Indeed/BuiltIn/etc.

Run the tool by invoking things at the command line with the name of the role/employer (text file) to which you wish to apply. For example, if a role is stored as `jobs/microsoft.txt`, run the following:

```
python generate.py microsoft
```

The generated cover letter will live at `output/microsoft.txt`.