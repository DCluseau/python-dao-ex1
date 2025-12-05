#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from business.school import School
from models.address import Address


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    school: School = School()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    #school.init_static()
    school.add_courses()

    # affichage de la liste des cours, leur enseignant et leurs élèves
    school.display_courses_list()

    print(school.get_course_by_id(1))
    print(school.get_course_by_id(2))
    print(school.get_course_by_id(9))
    new_address_street = "33 rue des péniches"
    if school.courses[1].teacher.address is not None:
        # A mettre dans school --> se baser sur add_courses
        school.courses[1].teacher.address.set(new_address_street, school.courses[1].teacher.address.city,
                                          school.courses[1].teacher.address.postal_code)
    #else:
    #    school.courses[1].teacher.address = Address(new_address_street, "",
    #     "")

if __name__ == '__main__':
    main()
