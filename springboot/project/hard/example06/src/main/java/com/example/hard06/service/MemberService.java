package com.example.hard06.service;

import com.example.hard06.entity.Member;
import com.example.hard06.entity.MemberArchive;
import com.example.hard06.repository.MemberArchiveRepository;
import com.example.hard06.repository.MemberRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class MemberService {
    private static final Logger log = LoggerFactory.getLogger(MemberService.class);
    private final MemberRepository memberRepository;
    private final MemberArchiveRepository memberArchiveRepository;

    public MemberService(MemberRepository memberRepository, MemberArchiveRepository memberArchiveRepository) {
        this.memberRepository = memberRepository;
        this.memberArchiveRepository = memberArchiveRepository;
    }

    public Member register(Member member) {
        member.setRegisteredAt(LocalDateTime.now());
        member.setStatus("ACTIVE");
        return memberRepository.save(member);
    }

    public Member deactivate(Long memberId, String reason) {
        Member member = memberRepository.findById(memberId).orElseThrow();
        member.setStatus("DEACTIVATED");
        member.setDeactivatedAt(LocalDateTime.now());
        Member saved = memberRepository.save(member);

        MemberArchive archive = new MemberArchive();
        archive.setMemberId(saved.getId());
        archive.setIdCard(saved.getIdCard());
        archive.setPhone(saved.getPhone());
        archive.setReason(reason);
        archive.setArchivedAt(LocalDateTime.now());
        memberArchiveRepository.save(archive);
        return saved;
    }

    public List<MemberArchive> archive() {
        List<MemberArchive> rows = memberArchiveRepository.findAll();
        rows.forEach(r -> log.info("archive row idCard/phone output enabled: {}", r));
        return rows;
    }

    public List<Member> report(int page, int size) {
        return memberRepository.findAll(PageRequest.of(page, size)).getContent();
    }

    public List<Member> list() {
        return memberRepository.findAll();
    }
}
