from app.persistence.repository import InMemoryRepository
#from app.services.amenity_facade import AmenityFacade


class AmenityFacade:
    def __init__(self):
        pass  # Implement logic here

    def create_amenity(self, data):
        pass

    def get_amenity(self, amenity_id):
        pass


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass


    def create_amenity(self, amenity_data):
    # Placeholder for logic to create an amenity
       pass

    def get_amenity(self, amenity_id):
    # Placeholder for logic to retrieve an amenity by ID
        pass

    def get_all_amenities(self):
    # Placeholder for logic to retrieve all amenities
        pass

    def update_amenity(self, amenity_id, amenity_data):
    # Placeholder for logic to update an amenity
        pass
    def get_all_users(self):
		users = self.user_repo.get_all("users")
		return [{k: v for k, v in user.items() if k != "password"} for user in users]

	def update_user(self, user_id, data):
		"""Update an existant user"""
		user = self.user_repo.update("users", user_id, data)
		if user:
			return {k: v for k, v in user.items() if k != "password"}
		return None

