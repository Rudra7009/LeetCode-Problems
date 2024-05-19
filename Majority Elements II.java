class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]))
            {
                map.put(nums[i],map.get(nums[i])+1);
            }
            else
            map.put(nums[i],1);
        }
        //iterate over the value associated with keys
          for(int hash:map.keySet())
          {  if(map.get(hash)>(nums.length/3))
            list.add(hash);
           }
           return list;
}
}
