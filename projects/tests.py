import os

from django.test import TestCase
from django.urls import reverse

from projects.models import Project

# Create your tests here.


def create_project(
        title: str ="Project Title",
        description: str = "Project description",
        technology: str = "technology",
        image: str = "boat.png"
):
    project = Project(
        title=title, description=description, technology=technology, image=image
    )
    project.save()

    return project


class ProjectIndexViewTests(TestCase):

    def test_no_projects(self):
        response = self.client.get(reverse("projects:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects yet!")
        self.assertQuerysetEqual(response.context["page_obj"], [])
        self.assertQuerysetEqual(response.context["project_list"], [])

    def test_projects_list(self):
        for _ in range(2):
            create_project()
        p = create_project()
        response = self.client.get(reverse("projects:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["page_obj"], [p.title]*3, transform=str)
        self.assertQuerysetEqual(response.context["project_list"], [p.title]*3, transform=str)

    def test_projects_pagination(self):
        for _ in range(19):
            create_project()
        p = create_project()
        response = self.client.get(reverse("projects:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["page_obj"], [p.title]*10, transform=str)
        self.assertQuerysetEqual(response.context["project_list"], [p.title] * 10, transform=str)

    def test_image_path_name_only(self):
        img_path = "image.png"
        project = create_project(image=img_path)
        self.assertEqual(project.image, img_path)

    def test_image_path_rel_path(self):
        img_path = "path/image.png"
        project = create_project(image=img_path)
        self.assertEqual(project.image, os.path.basename(img_path))

    def test_image_path_abs_path(self):
        img_path = "/path/image.png"
        project = create_project(image=img_path)
        self.assertEqual(project.image, os.path.basename(img_path))
