package com.example.medium06.service;
import com.example.medium06.dto.MemberHistoryDto;
import com.example.medium06.entity.Member;
import com.example.medium06.entity.MemberHistory;
import com.example.medium06.repository.MemberHistoryRepository;
import com.example.medium06.repository.MemberRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
@Service
public class MemberService {
    private static final Logger log=LoggerFactory.getLogger(MemberService.class);
    private final MemberRepository memberRepository;
    private final MemberHistoryRepository historyRepository;
    public MemberService(MemberRepository memberRepository,MemberHistoryRepository historyRepository){this.memberRepository=memberRepository;this.historyRepository=historyRepository;}
    public Member register(Member member){
        log.info("register phone={}, idCard={}",member.getPhone(),member.getIdCard());
        member.setStatus("ACTIVE");
        Member saved=memberRepository.save(member);
        MemberHistory h=new MemberHistory();h.setMember(saved);h.setActionType("REGISTER");historyRepository.save(h);
        return saved;
    }
    public Member cancel(Long memberId){
        Member m=memberRepository.findById(memberId).orElseThrow();
        m.setStatus("CANCELED");
        Member saved=memberRepository.save(m);
        MemberHistory h=new MemberHistory();h.setMember(saved);h.setActionType("CANCEL");historyRepository.save(h);
        return saved;
    }
    public Page<MemberHistoryDto> history(String keyword,int page,int size){
        return memberRepository.findByPhoneContainingOrInterestTagsContaining(keyword,keyword, PageRequest.of(page,size)).map(m->{
            MemberHistoryDto d=new MemberHistoryDto();
            d.id=m.getId();d.phone=m.getPhone();d.idCard=m.getIdCard();d.address=m.getAddress();d.interestTags=m.getInterestTags();d.actionType=m.getStatus();
            return d;
        });
    }
}
