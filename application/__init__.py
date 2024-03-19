import os
from concurrent import futures

import friend_service.friend_service_pb2 as friend_service_pb2
import friend_service.friend_service_pb2_grpc as friend_service_pb2_grpc
import grpc
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .model import Friend, Invite

load_dotenv()

engine = create_engine(os.getenv("DB_CONFIGURATION"))
Session = sessionmaker(bind=engine)


class FriendService(friend_service_pb2_grpc.FriendServiceServicer):
    def add_friend(self, request, context):
        session = Session()
        session.commit()
        session.close()
        return friend_service_pb2.AddFriendResponce(success=bool())

    def get_friends(self, request, context):
        session = Session()
        session.close()
        return friend_service_pb2.GetFriendsResponse()

    def remove_friend(self, request, context):
        session = Session()
        session.commit()
        session.close()
        return friend_service_pb2.RemoveFriendResponse(success=bool())

    def set_invite(self, request, context):
        session = Session()
        session.commit()
        session.close()
        return friend_service_pb2.SetInviteResponse(success=bool())

    def get_invites(self, request, context):
        session = Session()
        session.close()
        return friend_service_pb2.GetInvitesResponse()

    def update_invite_status(self, request, context):
        session = Session()
        session.commit()
        session.close()
        return friend_service_pb2.UpdateInviteStatusGesponse(success=bool())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    friend_service_pb2_grpc.add_FriendServiceServicer_to_server(FriendService(), server)
    server.add_insecure_port(f'[::]:{os.getenv("GRPC_PORT")}')
    print("start on", os.getenv("GRPC_PORT"))
    server.start()
    server.wait_for_termination()
