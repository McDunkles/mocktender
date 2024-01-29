package com.mocktender.controller;

import com.mocktender.model.LiquidContainerInfo;
import com.mocktender.repository.LiquidContainerInfoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Contains the API mappings and function calls that manipulate the 'LiquidContainerInfo' table in the database
 */
@RestController
@RequestMapping("api/lci")
public class LiquidContainerInfoController {

    @Autowired
    LiquidContainerInfoRepository lciRepo;

    @GetMapping("/getAll")
    public List<LiquidContainerInfo> getAllContainerInfo() {
        return lciRepo.findAll();
    }

    @GetMapping("/findByContainerNo")
    public LiquidContainerInfo findByContainerNo(@RequestParam("containerNo") int containerNo) {
        return lciRepo.findByContainerNo(containerNo).get(0);
    }


    @RequestMapping(value = "/addLCI", method = {RequestMethod.GET, RequestMethod.POST})
    public LiquidContainerInfo addLiquidContainerInfo(
            @RequestParam("containerNo") int containerNo, @RequestParam("liquid") String liquid) {

        LiquidContainerInfo lci = new LiquidContainerInfo(containerNo, liquid, 1000, 0);

        lciRepo.save(lci);
        return lci;
    }


    @RequestMapping(value = "/updateLiquidLevel", method = {RequestMethod.GET, RequestMethod.POST})
    public LiquidContainerInfo updateLiquidLevel(
            @RequestParam("containerNo") int containerNo, @RequestParam("liquidLevelPercentage") int liquidLevelPercentage) {

        System.out.println("Attempting to Update Liquid Level: {containerNo="+containerNo+", level = "+liquidLevelPercentage+"}");

        String liquid = this.findByContainerNo(containerNo).getLiquid();

        LiquidContainerInfo lci = new LiquidContainerInfo(containerNo, liquid, 1000, liquidLevelPercentage);

        System.out.println("Updating Liquid Level: {containerNo="+containerNo+", level = "+liquidLevelPercentage+"}");

        lciRepo.save(lci);
        return lci;
    }

}
