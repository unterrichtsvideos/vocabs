# Vocabulary used within the network of the meta-video portal unterrichtsvideos.net

This repository contains a collection of vocabularies used for a network of video portals in teacher education. These vocabularies are designed to standardize and categorize various aspects of classroom videos as well as teaching and learning resources with this context.

## Vocabularies

| Title               | Description                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------|
| Audience            | A value list for the audience of the Meta-Videoportal network.                                   |
| Camera perspectives | A value list for camera perspectives.                                                            |
| Educational levels  | A value list for the level in the education system as a teaching/learning context                |
| Grades              | A list of values for grades.                                                                     |
| Granularity         | Granularity of resource.                                                                         |
| Keywords            | A systematization of thematic keywords for educational resources in the context of the portals.  |
| Learning Format     | Learning/Teaching form.                                                                          |
| Lecture activities  | A list of values for teaching activities within the classroom                                    |
| Lecture phases      | A value list of lecture phases.                                                                  |
| License             | A value list of license types.                                                                |
| Material types      | A list of values for the types of materials that accompany educational resources.                |
| Portal providers    | A value list for the portal providers of the Meta-Videoportal network.                           |
| Resource types      | A value list for resource types of educational resources.                                        |
| School Subjects     | List of subjects in the school sector.                                                           |
| School topics       | A taxonomy of curriculum topics from the OpenEduHub.                                             |
| School Types        | A list of values for school types in the German school system.                                   |
| Time required       | A value list for the typical duration of engagement.                                             |
| Video types         | A value list for video types.                                                                    |

### Frameworks

| Title               | Description                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------|
| DigCompEdu          | European Framework for the Digital Competence of Educators                                       |
| DigCompEdu Observe  | Observation instrument for the European Framework for the Digital Competence of Educators        |
| Main-Teach-Model    | MAIN-Teach-Model for quality of teaching                                                         |

## Local validation

Create a virtual environment, install the validator dependency, and parse all TTL files:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

Then install dependencies and run the validation:

```bash
python -m pip install -r requirements.txt
python validate_vocabularies.py
```

Specific files or directories can also be checked:

```bash
python validate_vocabularies.py digCompEduObserve.ttl
python validate_vocabularies.py .
```
