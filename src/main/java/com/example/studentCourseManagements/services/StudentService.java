package com.example.studentCourseManagements.services;

import com.example.studentCourseManagements.dto.CreateStudentRequest;
import com.example.studentCourseManagements.dto.CreateStudentResponse;
import org.springframework.stereotype.Service;

public interface StudentService {


    CreateStudentResponse createStudent(CreateStudentRequest studentRequest);
}
