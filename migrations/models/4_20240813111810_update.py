from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `companies` ADD UNIQUE INDEX `uid_companies_name_1b02af` (`name`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `companies` DROP INDEX `idx_companies_name_1b02af`;"""
