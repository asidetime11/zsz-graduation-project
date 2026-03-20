package com.example.easy04.repository;

import com.example.easy04.entity.ResumeCandidate;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ResumeCandidateRepository extends JpaRepository<ResumeCandidate, Long> {
}
