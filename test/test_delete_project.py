from model.project import Project
import random

def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    # выбираем проект для удаления
    projects = app.project.get_projects_list()
    if len(projects) == 0:
        app.project.add_project(Project(name='Project_name', status='release', view_status='private',
                                        description='Project_description', inherit_global_categories=False))
    proj = random.choice(projects)

    app.project.delete_project(proj)
