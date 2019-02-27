import sqlite3

class Student:

    def __init__(self, firstname, lastname, gpa, major, facultyadvisor):
        self.firstname = firstname
        self.lastname = lastname
        self.gpa = gpa
        self.major = major
        self.facultyadvisor = facultyadvisor

    def __init__(self):
        self.data = []

    def getfirstname(self):
        return self.firstname

    def getlastname(self):
        return self.lastname

    def getgpa(self):
        return self.gpa

    def getmajor(self):
        return self.major

    def getfacultyadvisor(self):
        return self.facultyadvisor

    def gettuple(self):
        return self.firstname, self.lastname, self.gpa, self.major, self.facultyadvisor


