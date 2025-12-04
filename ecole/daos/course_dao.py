# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.course import Course
from daos.dao import Dao
from dataclasses import dataclass, field
from typing import Optional

from models.teacher import Teacher


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours course

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoie le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]
        
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course WHERE id_course=%s"
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        if record is not None:
            course = Course(record['name'], record['start_date'], record['end_date'])
            course.id = record['id_course']
        else:
            course = None

        return course

    @staticmethod
    def read_all():
        courses: list[Course] = []
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course"
            cursor.execute(sql)
            record = cursor.fetchall()
        if record is not None:
            for course in record:
                course_one = Course(course['name'], course['start_date'], course['end_date'])
                course_one.id = course['id_course']
                course_one.teacher = CourseDao().get_teacher(course_one.id)
                courses.append(course_one)
        else:
            courses = None
        return courses

    @staticmethod
    def get_teacher(id_course):
        """Renvoie le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""

        with Dao.connection.cursor() as cursor:
            sql = "SELECT id_teacher FROM course WHERE id_course=%s"
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        if record is not None:
            with Dao.connection.cursor() as cursor:
                id_teacher = record['id_teacher']
                sql = "SELECT hiring_date FROM teacher WHERE id_teacher=%s"
                cursor.execute(sql, id_teacher)
                record = cursor.fetchone()
                if record is not None:
                    hiring_date = record['hiring_date']
                else:
                    hiring_date = ""
                # Créer un objet Teacher
                sql = "SELECT teacher.id_teacher, person.first_name, person.last_name, person.age, address.street, address.city, address.postal_code FROM person LEFT OUTER JOIN address ON person.id_address = address.id_address LEFT OUTER JOIN teacher ON teacher.id_person = person.id_person WHERE teacher.id_teacher=%s"
                cursor.execute(sql, (id_teacher,))
                record = cursor.fetchone()
                if record is not None:
                    teacher = Teacher(record['first_name'], record['last_name'], record['age'], hiring_date)

        else:
            teacher = None
        return teacher

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
