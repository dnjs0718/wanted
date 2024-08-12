from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `languages` ADD `name` VARCHAR(30) NOT NULL;
        ALTER TABLE `languages` DROP COLUMN `full_name`;
        ALTER TABLE `languages` DROP COLUMN `short_name`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `languages` ADD `full_name` VARCHAR(255) NOT NULL;
        ALTER TABLE `languages` ADD `short_name` VARCHAR(100) NOT NULL;
        ALTER TABLE `languages` DROP COLUMN `name`;"""
