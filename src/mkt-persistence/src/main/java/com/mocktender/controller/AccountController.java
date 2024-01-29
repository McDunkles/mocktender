package com.mocktender.controller;

import com.mocktender.model.Account;
import com.mocktender.repository.AccountRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Contains the API mappings and function calls that manipulate the 'account' table in the database
 */
@RestController
@RequestMapping("api/account")
public class AccountController {

    @Autowired
    AccountRepository accountRepo;

    @GetMapping("/getAll")
    public List<Account> getAllAccounts() {
        return accountRepo.findAll();
    }

    @GetMapping("/findByName")
    public Account findByName(@RequestParam("username") String username) {
        return accountRepo.findByUsername(username).get(0);
    }

    @GetMapping("/findById")
    public Account findById(@RequestParam("id") String id) {

        Optional<Account> account = accountRepo.findById(id);

        return account.orElse(null);
    }


    @RequestMapping(value = "/addAccount", method = {RequestMethod.GET, RequestMethod.POST})
    public Account addAccount(
            @RequestParam("username") String username, @RequestParam("usertype") String usertype
    ) {

        int noAccounts = accountRepo.findAll().size();

        List<Account> allAccounts = accountRepo.findAll();

        boolean userAdded = false;
        String accountId = "";

        for (Account account : allAccounts) {
            if (account.getUsername().equalsIgnoreCase(username)) {
                userAdded = true;
                accountId = account.getId();
                break;
            } else {
                account.set_active(false);
            }
        }


        Account account;

        if (userAdded) {
            System.out.println("Account already exists...");
            account = new Account(accountId, username, usertype, true);
        } else {
            account = new Account(""+(noAccounts+1), username, usertype, true);
        }

        accountRepo.save(account);

        return account;
    }

    @GetMapping("/getActiveAccount")
    public Account getActiveAccount() {

        List<Account> allAccounts = accountRepo.findAll();

        Account activeAccount = null;

        for (Account account : allAccounts) {

            if (account.is_active()) {
                activeAccount = account;
                break;}
        }

        return activeAccount;
    }

}
