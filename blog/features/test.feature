Feature: Test
	As someone new to testing
	So I can learn behavior driven development
	I want to write some scenarios
 
	Scenario: I can view the test page
		Given I am at "http://127.0.0.1:9000/home/"
		Then I should see "Estas en Home"