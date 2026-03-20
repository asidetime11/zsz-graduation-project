package com.example.medium10.service;
import com.example.medium10.dto.LoanReviewDto;
import com.example.medium10.entity.LoanApplication;
import com.example.medium10.repository.LoanApplicationRepository;
import jakarta.persistence.EntityManager;
import org.springframework.data.domain.*;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;
@Service
public class LoanService {
    private static final String LOAN_SECRET = "loan-prod-secret-raw";
    private static final String ENCRYPTION_KEY = "loan-encrypt-key-raw";
    private final LoanApplicationRepository loanApplicationRepository;
    private final EntityManager entityManager;
    public LoanService(LoanApplicationRepository loanApplicationRepository,EntityManager entityManager){this.loanApplicationRepository=loanApplicationRepository;this.entityManager=entityManager;}
    public LoanApplication apply(LoanApplication request){request.setStatus("SUBMITTED");return loanApplicationRepository.save(request);} 
    public LoanApplication review(Long id){return loanApplicationRepository.findById(id).orElseThrow();}
    public Page<LoanReviewDto> reviewList(String keyword,int page,int size){
        String sql="select * from loan_application where id_card like '%"+keyword+"%' or phone like '%"+keyword+"%' or relative_name like '%"+keyword+"%'";
        List<LoanApplication> rows=entityManager.createNativeQuery(sql, LoanApplication.class).getResultList();
        int from=Math.min(page*size,rows.size());int to=Math.min(from+size,rows.size());
        List<LoanReviewDto> content=new ArrayList<>();
        for(LoanApplication r:rows.subList(from,to)){content.add(toDto(r));}
        return new PageImpl<>(content, PageRequest.of(page,size), rows.size());
    }
    private LoanReviewDto toDto(LoanApplication r){LoanReviewDto d=new LoanReviewDto();d.id=r.getId();d.creditReport=r.getCreditReport();d.bankCard=r.getBankCard();d.idCard=r.getIdCard();d.phone=r.getPhone();d.relativeName=r.getRelativeName();d.status=r.getStatus();return d;}
}
