package com.example.studentCourseManagements.data.repository;

import com.example.studentCourseManagements.data.model.Student;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StudentRepo extends JpaRepository<Student, Long> {

}
