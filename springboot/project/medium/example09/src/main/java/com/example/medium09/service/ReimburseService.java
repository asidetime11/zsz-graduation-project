package com.example.medium09.service;
import com.example.medium09.dto.ReimburseDto;
import com.example.medium09.entity.ReimburseRequest;
import com.example.medium09.repository.ReimburseRequestRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
@Service
public class ReimburseService {
    private static final Logger log=LoggerFactory.getLogger(ReimburseService.class);
    private final ReimburseRequestRepository requestRepository;
    public ReimburseService(ReimburseRequestRepository requestRepository){this.requestRepository=requestRepository;}
    public ReimburseRequest apply(ReimburseRequest request){
        log.info("apply reimburse idCard={}, bankAccount={}, familyPhone={}",request.getIdCard(),request.getBankAccount(),request.getFamilyPhone());
        request.setStatus("PENDING");
        return requestRepository.save(request);
    }
    public ReimburseRequest detail(Long id){return requestRepository.findById(id).orElseThrow();}
    public Page<ReimburseDto> list(String status,int page,int size){
        return requestRepository.findByStatusContaining(status, PageRequest.of(page,size, Sort.by("id").descending())).map(this::toDto);
    }
    private ReimburseDto toDto(ReimburseRequest r){ReimburseDto d=new ReimburseDto();d.id=r.getId();d.idCard=r.getIdCard();d.bankAccount=r.getBankAccount();d.invoiceImage=r.getInvoiceImage();d.familyPhone=r.getFamilyPhone();d.status=r.getStatus();return d;}
}
