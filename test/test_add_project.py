from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    app.project.add_project(Project(name='Project_name', status='release', view_status='private',
                                    description='Project_description', inherit_global_categories=False))
