from model.project import Project
import random

def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    # выбираем проект для удаления
    if len(app.project.get_projects_list()) == 0:
        app.project.add_project(Project(name='Project_name', status='release', view_status='private',
                                        description='Project_description', inherit_global_categories=False))
    old_projects = app.project.get_projects_list()
    projects = app.project.get_projects_list()
    proj = random.choice(projects)

    app.project.delete_project(proj)
    new_projects = app.project.get_projects_list()

    assert str(new_projects) not in str(old_projects)
