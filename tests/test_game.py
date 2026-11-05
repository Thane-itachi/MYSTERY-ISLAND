import unittest
from game import create_game, collect_item, move_player, can_cross_bridge, can_light_beacon, win_game, lose_game


class TestMysteryIsland(unittest.TestCase):

    def test_starting_game(self):
        location, energy, inventory = create_game()

        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)
        self.assertEqual(inventory, [])

    def test_collect_rope(self):
        inventory = []

        result = collect_item(inventory, "rope")

        self.assertTrue(result)
        self.assertIn("rope", inventory)

    def test_cannot_collect_same_item_twice(self):
        inventory = ["rope"]

        result = collect_item(inventory, "rope")

        self.assertFalse(result)
        self.assertEqual(inventory, ["rope"])

    def test_valid_movement(self):
        location, energy, moved = move_player("Beach", "Jungle", 5, [])


        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)

    def test_last_energy_point(self):
        location, energy, moved = move_player("Beach", "Jungle", 1, [])


        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 0)
        self.assertTrue(moved)
    

    def test_invalid_movement(self):
        location, energy, moved = move_player("Beach", "cave", 5, [])


        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 5)
        self.assertFalse(moved)

    
    def test_jungle_to_beach(self):
        location, energy, moved = move_player("Jungle", "beach", 5, [])

        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)

    def test_jungle_to_cave(self):
        location, energy, moved = move_player("Jungle", "cave", 5, [])

        self.assertEqual(location, "Cave")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)

    def test_cave_to_jungle(self):
        location, energy, moved = move_player("Cave", "jungle", 5, [])

        self.assertEqual(location, "Jungle")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)

    def test_cannot_cross_bridge_without_rope(self):
        location, energy, moved = move_player("Cave", "old bridge", 5, [])

        self.assertEqual(location, "Cave")
        self.assertEqual(energy, 5)
        self.assertFalse(moved)

    def test_can_cross_bridge_with_rope(self):
        location, energy, moved = move_player("Cave", "old bridge", 5, ["rope"])

        self.assertEqual(location, "Old Bridge")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)

    def test_old_bridge_to_lighthouse(self):
        location, energy, moved = move_player("Old Bridge", "lighthouse", 5, [])

        self.assertEqual(location, "Lighthouse")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)

    def test_lighthouse_to_old_bridge(self):
        location, energy, moved = move_player("Lighthouse", "old bridge", 5, [])

        self.assertEqual(location, "Old Bridge")
        self.assertEqual(energy, 4)
        self.assertTrue(moved)

    def test_cannot_move_with_zero_energy(self):
        location, energy, moved = move_player("Beach", "jungle", 0, [])

        self.assertEqual(location, "Beach")
        self.assertEqual(energy, 0)
        self.assertFalse(moved)    


    def test_bridge_requires_rope(self):
        inventory = []


        result = can_cross_bridge(inventory)

        self.assertFalse(result)


    def test_bridge_allows_player_with_rope(self):
        inventory = ["rope"]


        result = can_cross_bridge(inventory)

        self.assertTrue(result)


    def test_beacon_requires_lantern(self):
        inventory = []

        result = can_light_beacon(inventory)


        self.assertFalse(result)


    def test_beacon_allows_player_with_lantern(self):
        inventory = ["lantern"]


        result = can_light_beacon(inventory)


        self.assertTrue(result)


    def test_player_wins_at_lighthouse_with_lantern(self):
        result = win_game("Lighthouse", ["lantern"])
        self.assertTrue(result)

    def test_player_cannot_win_without_lantern(self):
        result = win_game("Lighthouse", [])
        self.assertFalse(result)

    def test_player_loses_when_energy_reaches_zero(self):
        result = lose_game(0)
        self.assertTrue(result)                               


if __name__ == "__main__":
    unittest.main()