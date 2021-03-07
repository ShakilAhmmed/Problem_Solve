<?php

class Solution {

    /**
     * @param String $command
     * @return String
     */
    function interpret($command) {
        $lookup = [
          "G"=>"G",
          "()"=>"o",
          "(al)"=>"al"
        ];
        $s = '';
        $s1 = '';
        $com = str_split($command);
        foreach($com as $cm) {
          $s1 .=$cm;
          if(array_key_exists($s1,$lookup)) {
            $s.=$lookup[$s1];
            $s1 = '';
          }
        }
        return $s;
    }
}
