function runUtilityClassUnitTests(){
    module("Utility Class Tests");

    test("doubleDigitPad", function(){
        equal(Utility.doubleDigitPad(1), "01");
        equal(Utility.doubleDigitPad(11), "11");
    });

    test("timecodeFormat", function(){
        equal(Utility.timecodeFormat(59), "00:59");
        equal(Utility.timecodeFormat(60), "01:00");
    });



}