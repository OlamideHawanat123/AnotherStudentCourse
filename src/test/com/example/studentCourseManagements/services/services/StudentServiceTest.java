package com.example.studentCourseManagements.services.services;
import com.example.studentCourseManagements.dto.CreateStudentRequest;
import com.example.studentCourseManagements.dto.CreateStudentResponse;
import com.example.studentCourseManagements.services.StudentService;
import lombok.AllArgsConstructor;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
public class StudentServiceTest {

    @Autowired
    private StudentService studentService;

    @Test
    public void testToCreateStudent() {

    CreateStudentRequest studentRequest = new CreateStudentRequest();
    studentRequest.setFullName("John Doe");
    studentRequest.setEmail("john.doe@example.com");
    studentRequest.setPassword("JohnDoe");

    CreateStudentResponse response = studentService.createStudent(studentRequest);
    assertNull(response);



    }
}
