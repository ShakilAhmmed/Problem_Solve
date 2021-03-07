<?php

class Solution {

    /**
     * @param String[][] $items
     * @param String $ruleKey
     * @param String $ruleValue
     * @return Integer
     */
    function countMatches($items, $ruleKey, $ruleValue) {
        $look_up = [
          0 => "type",
          1 => "color",
          2 => "name"
        ];
        $count = 0;
        foreach($items as $key=>$item) {
          if(($ruleKey === "type" && $item[0] === $ruleValue) ||
             ($ruleKey === "color" && $item[1] === $ruleValue) ||
             ($ruleKey === "name" && $item[2] === $ruleValue)
          ) {
            $count ++;
          }
        }
        return $count;
    }
}

$obj = new Solution();
echo $obj->countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color","silver");
