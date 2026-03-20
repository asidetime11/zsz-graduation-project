package com.example.medium06.repository;
import com.example.medium06.entity.Member;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
public interface MemberRepository extends JpaRepository<Member, Long> {
    Page<Member> findByPhoneContainingOrInterestTagsContaining(String phone,String interestTags, Pageable pageable);
}
