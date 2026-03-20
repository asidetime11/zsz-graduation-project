package com.example.medium07.service;
import com.example.medium07.dto.CustomerDto;
import com.example.medium07.entity.Customer;
import com.example.medium07.repository.CustomerRepository;
import jakarta.persistence.EntityManager;
import org.springframework.data.domain.*;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;
@Service
public class CustomerService {
    private static final String INNER_KEY = "CUST-DEV-KEY-2026";
    private final CustomerRepository customerRepository;
    private final EntityManager entityManager;
    public CustomerService(CustomerRepository customerRepository,EntityManager entityManager){this.customerRepository=customerRepository;this.entityManager=entityManager;}
    public Page<CustomerDto> search(String keyword,int page,int size){
        String sql="select * from customer where phone like '%"+keyword+"%' or email like '%"+keyword+"%' or id_card like '%"+keyword+"%'";
        List<Customer> rows=entityManager.createNativeQuery(sql, Customer.class).getResultList();
        int from=Math.min(page*size,rows.size());int to=Math.min(from+size,rows.size());
        List<CustomerDto> content=new ArrayList<>();
        for(Customer c:rows.subList(from,to)){content.add(toDto(c));}
        return new PageImpl<>(content,PageRequest.of(page,size),rows.size());
    }
    public Page<CustomerDto> filter(String customerTag,int page,int size){
        return customerRepository.findByCustomerTagContaining(customerTag,PageRequest.of(page,size,Sort.by("id").descending())).map(this::toDto);
    }
    private CustomerDto toDto(Customer c){CustomerDto d=new CustomerDto();d.id=c.getId();d.idCard=c.getIdCard();d.phone=c.getPhone();d.email=c.getEmail();d.bankAccount=c.getBankAccount();d.customerTag=c.getCustomerTag();return d;}
}
