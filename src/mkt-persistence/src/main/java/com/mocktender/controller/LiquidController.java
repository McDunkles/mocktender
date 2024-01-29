package com.mocktender.controller;

import com.mocktender.model.Liquid;
import com.mocktender.repository.LiquidRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Contains the API mappings and function calls that manipulate the 'liquid' table in the database
 */
@RestController
@RequestMapping("api/liquids")
public class LiquidController {

    @Autowired
    LiquidRepository liquidRepo;

    @GetMapping("/findAll")
    public List<Liquid> findAllLiquids() {
        return liquidRepo.findAll();
    }

    @GetMapping("/findByName")
    public List<Liquid> findByName(@RequestParam("name") String name) {
        return liquidRepo.findByName(name);
    }


    @RequestMapping(value = "/addLiquid", method = {RequestMethod.GET, RequestMethod.POST})
    public Liquid addLiquid(
            @RequestParam("name") String name
    ) {
        Liquid liquid = new Liquid(name);

        liquidRepo.save(liquid);
        return liquid;
    }

}
