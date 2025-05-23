package com.example.studentCourseManagements.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CreateStudentRequest {
    private String fullName;
    private String email;
    private String password;
}
