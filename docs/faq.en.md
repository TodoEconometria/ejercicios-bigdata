# Frequently Asked Questions (FAQ)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​​​‌‍​‌‌​​‌​​‍​‌‌​​‌​‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​​‌​﻿

Answers to the most common questions about the course.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​​​‌‍​‌‌​​‌​​‍​‌‌​​‌​‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​​‌​﻿

---

## General

### Do I need prior experience in Big Data?

**No.** The course starts from scratch. You only need:

- Basic Python knowledge
- Ability to use the terminal/console
- Willingness to learn

!!! tip "Don't have Python?"
    Go to the [Installation Guide](guia-inicio/instalacion.md) where we explain how to install everything from scratch.

---

### How long does it take to complete the exercises?

**It depends on your level:**

| Level | Total Time | Hours/Week | Duration |
|-------|------------|------------|----------|
| Beginner | 120-140 hours | 10-15h | 10-12 weeks |
| Intermediate | 60-80 hours | 8-10h | 6-8 weeks |
| Advanced | 40-50 hours | 5-8h | 4-5 weeks |

**No rush.** Learn at your own pace. The important thing is to understand each concept well.

---

### Is the data real or synthetic?

**Real.** We use real public datasets:

- NYC Taxi & Limousine Commission (TLC)
- Weather data from NOAA
- Other public datasets from Kaggle

This gives you experience with real-world data (dirty, incomplete, large).

---

### Can I use this in my portfolio?

**Yes!** In fact, we recommend it.

Many students have landed jobs by showcasing:

- Their exercise solutions
- The dashboard they created
- Their GitHub fork with professional commits

!!! tip "Tip"
    Make your fork public and add a personalized README explaining your learning journey.

---

### Is there a certificate upon completion?

**For in-person course students:** Yes, a 230-hour certificate.

**For self-learners:** There is no official certificate, but your GitHub is your certificate. Employers value seeing your code more than a PDF.

!!! success "Your GitHub is Your Certificate"
    - Professional commits
    - Well-documented code
    - Complete projects
    - Active contributions

---

## Technical

### What computer do I need?

**Minimum:**

- 8GB RAM
- 20GB disk space
- i5 processor or equivalent
- Windows 10+, macOS 10.14+, or Linux (Ubuntu 20.04+)

**Recommended:**

- 16GB RAM
- 50GB SSD disk space
- i7 processor or equivalent

!!! info "Don't have good hardware?"
    You can use Google Colab or GitHub Codespaces (free) to work in the cloud.

---

### Does it work on Windows/Mac/Linux?

**Yes.** The course is compatible with all three operating systems.

- **Windows:** Preferably Windows 10 or higher
- **macOS:** macOS 10.14 (Mojave) or higher
- **Linux:** Ubuntu 20.04+, Fedora, Arch, etc.

The [Installation Guide](guia-inicio/instalacion.md) has specific instructions for each system.

---

### Can I use another IDE instead of PyCharm?

**Yes.** PyCharm is recommended but not required.

Alternatives:

- **Visual Studio Code** - Lightweight and very popular
- **Jupyter Lab** - Excellent for notebooks
- **Sublime Text** - Advanced text editor
- **Vim/Emacs** - If you are an advanced user

The important thing is that you feel comfortable with your tool.

---

### How do I download the data?

The data is downloaded automatically with a script:

```bash
# Ir a la carpeta de datos
cd datos

# Ejecutar script de descarga
python descargar_datos.py
```

The script automatically downloads and decompresses all the required datasets.

!!! warning "Disk space"
    The complete datasets take up ~5GB. Make sure you have enough space.

---

## Git and GitHub

### I have never used Git. Is it very difficult?

**It is not difficult**, but it requires practice.

We have complete step-by-step guides:

1. [Fork and Clone](git-github/fork-clone.md) - The basics
2. [Your First Exercise](guia-inicio/primer-ejercicio.md) - Complete workflow
3. [Useful Commands](git-github/comandos-utiles.md) - Quick reference

!!! tip "Learn by doing"
    The best way to learn Git is by using it. Your first commits will feel awkward, but you improve quickly.

---

### What is a Fork? Why do I need one?

**Fork** = Your personal copy of the repository on GitHub.

You need it because:

- :lock: You cannot modify the instructor's repository directly
- :pencil2: The fork is YOUR space to work
- :arrows_counterclockwise: You can sync it with the original
- :outbox_tray: The system automatically evaluates your PROMPTS in your fork

See the full guide: [Fork and Clone](git-github/fork-clone.md)

---

### How do I keep my Fork up to date?

When the instructor adds new exercises, you need to sync your fork.

**Easy method (GitHub Web):**

1. Go to your fork on GitHub
2. Click "Sync fork" → "Update branch"
3. On your PC: `git pull origin main`

**Full method (Terminal):**

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

See the full guide: [Sync Fork](git-github/sincronizar-fork.md)

---

### I made a bad commit. How do I undo it?

**Before pushing:**

```bash
# Deshacer ultimo commit (mantiene cambios)
git reset --soft HEAD~1

# Deshacer ultimo commit (descarta cambios)
git reset --hard HEAD~1
```

**After pushing:**

```bash
# Crear nuevo commit que revierte el anterior
git revert HEAD
git push origin tu-rama
```

!!! danger "Avoid force push"
    Never use `git push --force` on shared branches or open Pull Requests.

---

## Exercises

### I cannot complete an exercise. What should I do?

**Step 1:** Read the error carefully

Most of the time the error tells you exactly what is wrong.

**Step 2:** Search on Google

Copy the error message and search for it. Someone else has probably had it before.

**Step 3:** Check the documentation

- [Pandas Docs](https://pandas.pydata.org/docs/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python Docs](https://docs.python.org/3/)

**Step 4:** Ask for help

- **In-person students:** Ask during class
- **Self-learners:** Create an Issue on GitHub explaining your problem

!!! tip "How to ask for help"
    Include:

    - What you tried to do
    - What error you got (full message)
    - What you have already tried
    - Your relevant code

---

### Can I do the exercises out of order?

**Not recommended.** The exercises are designed to:

- Build upon previous knowledge
- Gradually increase in difficulty
- Introduce concepts in a logical order

!!! warning "Exception"
    If you already have experience with Python and Pandas, you can start at LEVEL 2 (Exercise 03).

---

### How many times can I attempt an exercise?

**As many as you need.** There is no limit on attempts.

The goal is to **learn**, not to pass quickly.

- You can update your fork as many times as you want with `git push`
- The automatic evaluation system checks your PROMPTS.md file
- You learn more from mistakes than from successes

---

### Can I use additional libraries?

**Yes**, but:

1. Justify why you need them
2. Add them to `requirements.txt`
3. Document how to install them
4. Mention in PROMPTS.md which libraries you used

!!! example "Example"
    If you use `seaborn` for visualizations:

    ```python
    # requirements.txt
    pandas==2.0.0
    seaborn==0.12.0  # Para visualizaciones avanzadas
    ```

    And in your `PROMPTS.md` file mention: "I used seaborn to create more professional charts"

---

## Support

### Do you offer support if I get stuck?

**For in-person course students:**

- :white_check_mark: Full support during sessions
- :white_check_mark: Email consultations
- :white_check_mark: Automatic submission review

**For self-learners:**

- :x: No direct support
- :white_check_mark: You can create Issues on GitHub
- :white_check_mark: The community can help you
- :white_check_mark: Complete documentation available

---

### How do I contact the instructor?

**For course inquiries:**

- GitHub Issues: [Create Issue](https://github.com/TodoEconometria/ejercicios-bigdata/issues)
- Email: cursos@todoeconometria.com

**For business consulting:**

- Email: cursos@todoeconometria.com
- LinkedIn: [Juan Gutierrez](https://www.linkedin.com/in/juangutierrezconsultor/)
- Web: [TodoEconometria](https://www.todoeconometria.com)

!!! warning "Response time"
    - In-person students: 24-48 hours
    - Self-learners via Issues: When available
    - Businesses: 24 hours

---

## Technical Issues

### Python is not recognized as a command

**Windows:**

1. Reinstall Python
2. Check "Add Python to PATH"
3. Restart the terminal

**macOS/Linux:**

Use `python3` instead of `python`:

```bash
python3 --version
pip3 install pandas
```

---

### Error: ModuleNotFoundError

**Cause:** You did not install the dependencies.

**Solution:**

```bash
# Activa el entorno virtual
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate      # Windows

# Instala dependencias
pip install -r requirements.txt
```

---

### Git says "fatal: not a git repository"

**Cause:** You are not in the project folder.

**Solution:**

```bash
# Navega a la carpeta correcta
cd path/to/ejercicios-bigdata

# Verifica
git status  # Deberia funcionar
```

---

### I cannot push: "Permission denied"

**Cause:** Authentication issues with GitHub.

**Quick solution (HTTPS):**

```bash
# Cambiar a HTTPS
git remote set-url origin https://github.com/TU_USUARIO/ejercicios-bigdata.git

# Intentar push de nuevo
git push origin tu-rama
```

**Permanent solution (SSH):**

Configure SSH keys: [GitHub SSH Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

### The dashboard does not load the data

**Check:**

1. Does the database exist?
   ```bash
   ls datos/taxi.db
   ```

2. Is Flask running?
   ```bash
   python app.py
   ```

3. Correct port? (default: 5000)
   ```
   http://localhost:5000
   ```

4. Check the browser error console (F12)

---

## Career and Employment

### Will this course help me get a job?

**It can help a lot**, especially if:

- You complete all exercises with quality
- You create a professional dashboard
- You document your code well
- You maintain an active GitHub

!!! success "What employers value"
    1. **Project portfolio** (your GitHub)
    2. **Clean, documented code**
    3. **Experience with real data**
    4. **Problem-solving ability**

A well-crafted repository is worth more than 10 certificates.

---

### What jobs can I get with these skills?

With the skills from this course you can apply for:

- **Data Analyst** - Data analysis with Python/SQL
- **Junior Data Scientist** - Modeling and advanced analysis
- **Data Engineer** - ETL pipelines, data processing
- **Business Intelligence Developer** - Dashboards and reports
- **Python Developer** - Backend development with data

---

### Do I need a university degree?

**It depends on the employer.**

- **Tech companies:** Value portfolio over degree
- **Traditional companies:** May require a degree
- **Startups:** Portfolio > Degree
- **Freelance:** Only your work matters

!!! tip "Compensating for lack of a degree"
    - Solid GitHub portfolio
    - Relevant certifications
    - Impressive personal projects
    - Open source contributions

---

## Other

### Can I share my solution publicly?

**Yes**, but consider:

- **After completing:** Share after receiving your grade
- **With credits:** Mention that it is from the TodoEconometria course
- **No spoilers:** Do not share solutions to help others cheat

!!! success "Sharing is good"
    Sharing your code helps:

    - Others to learn
    - Build your personal brand
    - Demonstrate skills to employers

---

### Is the course updated?

**Yes.** The repository is updated regularly with:

- New exercises
- Improvements to existing ones
- Library updates
- New datasets
- Bug fixes

Keep your fork synced to get updates: [Sync Fork](git-github/sincronizar-fork.md)

---

### Can I contribute to the course?

**Yes!** Contributions are welcome.

You can contribute by:

- :bug: Reporting bugs via Issues
- :pencil: Improving documentation
- :bulb: Suggesting new exercises
- :art: Sharing your dashboard in the gallery

See the [Contributions](index.md#contributions) section

---

### Where can I learn more?

**Recommended resources:**

- [Python for Data Analysis](https://wesmckinney.com/book/) - Book by Wes McKinney
- [SQL Tutorial](https://mode.com/sql-tutorial/) - Interactive SQL
- [Dask Tutorial](https://tutorial.dask.org/) - Official Dask tutorial
- [r/datascience](https://www.reddit.com/r/datascience/) - Reddit community

**Complementary courses:**

- [Python for Data Science (Coursera)](https://www.coursera.org/specializations/python)
- [SQL for Data Science (DataCamp)](https://www.datacamp.com/courses/intro-to-sql-for-data-science)
- [Apache Spark (Udacity)](https://www.udacity.com/course/learn-spark-at-udacity--ud2002)

---

## Unanswered Questions?

!!! question "Didn't find your answer?"

    **In-person students:** Ask in the next session or send an email

    **Self-learners:** Create an Issue on GitHub:

    [Create Issue](https://github.com/TodoEconometria/ejercicios-bigdata/issues/new){ .md-button .md-button--primary }

    Include:
    - Descriptive title
    - Detailed description of your question
    - Context (which exercise, what you tried, etc.)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​​​‌‍​‌‌​​‌​​‍​‌‌​​‌​‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​​‌​﻿---

## Additional Resources

- [Getting Started Guide](guia-inicio/index.md) - Start from scratch
- [Git and GitHub](git-github/index.md) - Git guides
- [Exercises](ejercicios/index.md) - Exercise list
- [Roadmap](guia-inicio/roadmap.md) - Study plan
