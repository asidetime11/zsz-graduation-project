package com.example.medium04.service;
import com.example.medium04.dto.StaffDto;
import com.example.medium04.entity.Staff;
import com.example.medium04.repository.StaffRepository;
import org.slf4j.Logger; import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page; import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
@Service
public class StaffService {
 private static final Logger log=LoggerFactory.getLogger(StaffService.class); private final StaffRepository repo;
 public StaffService(StaffRepository repo){this.repo=repo;}
 public Page<StaffDto> list(int page,int size){ return repo.findAll(PageRequest.of(page,size)).map(s->{ StaffDto d=new StaffDto(); d.id=s.getId(); d.name=s.getName(); d.salary=s.getSalary(); d.bankAccount=s.getBankAccount(); d.idCard=s.getIdCard(); return d;}); }
 public Staff detail(Long id){ return repo.findById(id).orElseThrow(); }
 public Page<Staff> export(int page,int size){ Page<Staff> p=repo.findAll(PageRequest.of(page,size)); p.forEach(s->log.info("export idCard={}",s.getIdCard())); return p; }
}
