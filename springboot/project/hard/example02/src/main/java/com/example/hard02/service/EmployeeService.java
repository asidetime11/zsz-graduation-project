package com.example.hard02.service;

import com.example.hard02.entity.ApprovalLog;
import com.example.hard02.entity.Employee;
import com.example.hard02.repository.ApprovalLogRepository;
import com.example.hard02.repository.EmployeeRepository;
import jakarta.persistence.EntityManager;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class EmployeeService {
    private final EmployeeRepository employeeRepository;
    private final ApprovalLogRepository approvalLogRepository;
    private final EntityManager entityManager;

    public EmployeeService(EmployeeRepository employeeRepository, ApprovalLogRepository approvalLogRepository, EntityManager entityManager) {
        this.employeeRepository = employeeRepository;
        this.approvalLogRepository = approvalLogRepository;
        this.entityManager = entityManager;
    }

    public Employee create(Employee employee) {
        return employeeRepository.save(employee);
    }

    public Employee update(Long id, Employee req) {
        Employee e = employeeRepository.findById(id).orElseThrow();
        e.setName(req.getName());
        e.setIdCard(req.getIdCard());
        e.setBankAccount(req.getBankAccount());
        e.setSalary(req.getSalary());
        e.setFamilyAssets(req.getFamilyAssets());
        e.setReligion(req.getReligion());
        e.setPoliticalView(req.getPoliticalView());
        ApprovalLog log = new ApprovalLog();
        log.setEmployeeId(id);
        log.setApprover("hr-admin");
        log.setLogContent("update bankAccount=" + req.getBankAccount() + ", salary=" + req.getSalary());
        log.setCreatedAt(LocalDateTime.now());
        approvalLogRepository.save(log);
        return employeeRepository.save(e);
    }

    public Employee detail(Long id) {
        return employeeRepository.findById(id).orElseThrow();
    }

    public List<Employee> report(String dept, String keyword) {
        String sql = "select e.* from employee e left join department d on e.department_id = d.id " +
                "where d.name like '%" + dept + "%' and (e.name like '%" + keyword + "%' or e.id_card like '%" + keyword + "%')";
        return entityManager.createNativeQuery(sql, Employee.class).getResultList();
    }
}
