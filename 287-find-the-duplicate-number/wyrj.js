/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let oneStep = 0, twoStep = 0;
    while (true) {
        twoStep = nums[nums[twoStep]];
        oneStep = nums[oneStep];
        if (twoStep === oneStep) break;
    }
    oneStep = 0;
    while (oneStep !== twoStep) {
        twoStep = nums[twoStep];
        oneStep = nums[oneStep];
    }
    return oneStep;
};
